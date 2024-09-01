from Chicken_Disease_Classification.config.configuration import ConfigurationManager
from Chicken_Disease_Classification.components.evaluation import Evaluation
from Chicken_Disease_Classification import logger


STAGE_NAME= "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):  # initializing empty constructor
        pass

    def main(self):
        config=ConfigurationManager()
        val_config=config.get_validation_config()
        evaluation=Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
            

# For integrating DVC we will use in this way
if __name__ =='__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj=EvaluationPipeline()  # Calling the class
        obj.main()                           # Calling the main method
        logger.info(f" Stage {STAGE_NAME} Completed")

    except Exception as e:
        logger.exception(e)
        raise e
    
# call the pipeline in main.py
