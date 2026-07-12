import logging
import os


class TourismLogger:

    def __init__(self):
        self.log_folder = "logs"
        self.log_file = "logs/tourism_pulse.log"

    def setup_logger(self):
        try:
            os.makedirs(
                self.log_folder,
                exist_ok=True
            )

            logging.basicConfig(
                filename=self.log_file,
                level=logging.INFO,
                format=(
                    "%(asctime)s - "
                    "%(levelname)s - "
                    "%(message)s"
                )
            )

            logger = logging.getLogger(
                "TourismPulse"
            )

            logger.info(
                "TourismPulse logging initialized."
            )

            print("Logger initialized successfully.")
            print(
                f"Log file created at: {self.log_file}"
            )

            return logger

        except Exception as error:
            print("Error setting up logger:", error)
            return None


if __name__ == "__main__":

    logger_config = TourismLogger()

    logger = logger_config.setup_logger()

    if logger:
        logger.info(
            "Tourism data analysis started."
        )

        logger.warning(
            "Sample tourism warning recorded."
        )

        logger.info(
            "Tourism data analysis completed."
        )

        print("Sample log messages recorded successfully.")