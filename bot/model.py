class Restaurant:
  def __init__(self, name, location, dishes, specialty, ambience, nationality, qualification, criticReview, peopleCapacity, peopleInside, averagePrice, dresscode):
      self.name = name
      self.specialty = specialty
      self.location = location
      self.dishes = dishes
      self.ambience = ambience
      self.nationality = nationality
      self.qualification = qualification
      self.criticReview = criticReview
      self.peopleCapacity = peopleCapacity
      self.peopleInside = peopleInside
      self.averagePrice = averagePrice
      self.dresscode = dresscode

  def getName(self):
      return self.name

  def getSpecialty(self):
      return self.specialty

  def getLocation(self):
      return self.location

  def getDishes(self):
      return self.dishes

  def getAmbience(self):
      return self.ambience

  def getNationality(self):
      return self.nationality

  def getQualification(self):
      return self.qualification

  def getCriticReview(self):
    return self.criticReview

  def getPeopleCapacity(self):
    return self.peopleCapacity

  def getPeopleInside(self):
    return self.peopleInside

  def getAveragePrice(self):
    return self.averagePrice

  def getDresscode(self):
    return self.dresscode



class Location:

  def __init__(self, city, country, environment):
        self.city = city
        self.country = country
        self.environment = environment #E.g. Seaside, Centric, Mountain, Village

  def getCity(self):
      return self.city

  def getCountry(self):
      return self.country

  def getEnvironment(self):
      return self.environment