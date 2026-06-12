# FIRST LOG......

# import logging
# logging.warning("This is warning")

#LOGGER>>>>>

# import logging
# logger = logging.getLogger()
# print(logger)

# import logging

# logging.debug("variable x = 10")
# logging.info("user login")
# logging.warning("Disk space is low")
# logging.error("internet disconnected")
# logging.critical("server crashed")

# CHANGING LOGGING LEVEL BECAUSE DEBUG AND INFO NOT SHOWN >>>>>>>

# import logging

# logging.basicConfig(level=logging.DEBUG)

# logging.debug("variable x = 10")
# logging.info("user login")
# logging.warning("Disk space is low")

# COMMON PARAMETER OF BASICCONFIG(.  )

# import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format= " %(levelname)s - %(message)s"
#                     )


# logging.warning("Disk space is low")

#LOGGING TO FILEEE....


# import logging

# logging.basicConfig(
#     filename="app.log",
#     filemode="w",
#     level=logging.DEBUG,
#     format=
#     "%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.info("Program Started")

# logging.warning("Low Memory")

# logging.error("Database Failed")

#COMPLETE professional example of logging....

import logging

logging.basicConfig(
    filename="student.log",
    level=logging.DEBUG,
    format=
    "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started ")

student = "mohit chaudhary"

logging.info(
    "Student Logged In: %s",
    student
)

try:
    result = 10/0

except Exception:
    logging.exception("calculation error")

logging.info("Application closed")