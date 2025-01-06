import json

import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod


class BookDisplay(ABC):
    def __init__(self, content: str):
        self.content = content

    @abstractmethod
    def display(self, display_type: str) -> None:
        if display_type == "console":
            print(self.content)
        elif display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")


class BookPrint(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @abstractmethod
    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            print(self.content)
        elif print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class BookSerializer(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @abstractmethod
    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        elif serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.title
            content = ET.SubElement(root, "content")
            content.text = self.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


class Book(BookSerializer, BookDisplay, BookPrint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def serialize(self, serialize_type: str) -> str:
        return super().serialize(serialize_type)

    def display(self, display_type: str) -> None:
        super().display(display_type)

    def print_book(self, print_type: str) -> None:
        super().print_book(print_type)
