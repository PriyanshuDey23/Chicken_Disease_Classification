import tensorflow as tf
from pathlib import Path
from Chicken_Disease_Classification.entity.config_entity import EvaluationConfig
from Chicken_Disease_Classification.utils.common import save_json


class Evaluation:
    def __init__(self,config:EvaluationConfig):
        self.config=config

    def _valid_generator(self):

        datagenerator_kwargs=dict(
            rescale=1./255,     # Normalization
            validation_split=0.20
        )

        dataflow_kwargs=dict(
            target_size=self.config.params_image_size[:-1], # [224, 224]
            batch_size=self.config.params_batch_size,
            interpolation="bilinear" # Fill the gaps
        )

        valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator=valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path:Path) -> tf.keras.Model: # Load the model
        return tf.keras.models.load_model(path)
    
    def evaluation(self):  # Evaluation
        model=self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score=model.evaluate(self.valid_generator)

    def save_score(self):     # Save the score in json format
        scores={"Loss": self.score[0], "accuracy":self.score[1]}
        save_json(path=Path("scores.json"),data=scores)

    