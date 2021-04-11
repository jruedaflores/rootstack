from flask_googlemaps import icons
import random


class Job(object):
    def __init__(self, id, title, description, latitude, longitude, image, date, status, assigned_to, created_at,
                 updated_at, *args, **kwargs):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__latitude = latitude
        self.__longitude = longitude
        self.__image = image
        self.__date = date
        self.__status = status
        self.__assigned_to = assigned_to
        self.__created_at = created_at
        self.__updated_at = updated_at

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @property
    def image(self):
        return self.__image

    @property
    def date(self):
        return self.__date

    @property
    def status(self):
        return self.__status

    @property
    def assigned_to(self):
        return self.__assigned_to

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    def get_values(self):
        return [
            self.__id,
            self.__title,
            self.__description,
            self.__date,
            self.__status,
        ]

    def get_marker(self):
        icon = f'//chart.apis.google.com/chart?chst=d_map_pin_letter&chld={self.__id}|FE6256|000000'
        return {
            'icon': icon,
            "title": self.__title,
            'lat': self.__latitude,
            'lng': self.__longitude,
            'infobox': (
                f"<h3>{self.__title}</h3>"
                f"{self.__description}"
            )
        }
