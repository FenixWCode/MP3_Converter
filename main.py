import const
from monitoring import DirMonitor


if __name__ == "__main__":
    d1 = DirMonitor(const.CONTAINER_DIRECTORY)
    print("The MP3 converter is running...")
    d1.monitor()

