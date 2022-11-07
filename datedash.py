class Dates:

  def __init__(self, date):
    self.__date = date

  def get(cls):
    return cls.__date

  @staticmethod
  def change(date):
        return date.replace("/" , ".")

date = Dates("5/8/1995")
date_db = "5.8.1995"
dateWD = Dates.change(date_db)

print(dateWD)