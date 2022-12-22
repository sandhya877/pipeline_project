
from housing.logger import logging

from housing.pipeline.pipeline import Pipeline

def main():
    try:
        # config_path = os.path.join("config","config.yaml")
        # pipeline = Pipeline(Configuartion(config_file_path=config_path))
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # pipeline.start()
        logging.info("main function execution completed.")

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()

