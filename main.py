from typing import List, Optional
from fastapi import FastAPI
import typer
import pkgutil
import importlib
import commands
import os
import inspect
from functools import wraps
from lib.command import BaseCommand

app = FastAPI()

command_line = typer.Typer()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def register(cmd_cls, namespace="app"):
    sig = inspect.signature(cmd_cls.__init__)
    new_params = []

    for name, param in sig.parameters.items():
        if name == "self": continue

        if isinstance(param.default, BaseCommand.Option):
            # TRANSLATION LAYER: Map our generic Option to Typer's Option
            # This passes ALL kwargs (help, prompt, etc.) directly to Typer
            typer_opt = typer.Option(
                param.default.default, 
                **param.default.metadata
            )
            new_params.append(param.replace(default=typer_opt))
        else:
            new_params.append(param)

    # Reconstruct signature and inject into the runner
    new_sig = sig.replace(parameters=new_params)

    def _run(*args, **kwargs):
        cmd_cls(*args, **kwargs).run()

    _run.__signature__ = new_sig
    command_line.command(name=f"{namespace}:{cmd_cls.command}")(_run)

if __name__ == "__main__":

    for type, name, f in pkgutil.iter_modules(commands.__path__):
        if os.path.isdir(f"commands/{name}") :
            for type, inner_name, s in pkgutil.iter_modules([os.path.abspath(f"commands/{name}")]):
                module = importlib.import_module(f"commands.{name}.{inner_name}")
                if hasattr(module, "Command"):
                    register(module.Command, name)
        else:
            module = importlib.import_module(f"commands.{name}")
            if hasattr(module, "Command"):
                register(module.Command)

    command_line()