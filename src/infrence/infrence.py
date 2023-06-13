import gradio as gr
from transformers import pipeline, set_seed
from ray.serve.gradio_integrations import GradioServer
from ray import serve
import os
from src.infrence.schemas import Launcher
from aviary.backend.server.run import run


class Infrence():
    def __gradio_summarizer_builder():
        task = "summarization"
        model = "t5-small"
        model_path = os.path.join("/Users/lipeng/workspaces/github.com/vincent-pli/platform", "pretrained", task, model)
        generator = None

        if os.path.isdir(model_path):
            print("loading from local, since the model is already there...")
            generator = pipeline(task, model=model_path)
        else:
            generator = pipeline(task, model=model)
            os.makedirs(model_path)
            generator.save_pretrained(model_path)

        set_seed(42)

        return gr.Interface.from_pipeline(generator)
    
    def run(self, launcher: Launcher):
        # app = GradioServer.options(name = launcher.name, ray_actor_options={"num_cpus": 4}).bind(
        #     self.__gradio_summarizer_builder
        # )   

        # serve.run(app)
        run("/Users/lipeng/workspaces/github.com/vincent-pli/platform/pretrained/amazon--LightGPT.yaml")
