from abc import ABC, abstractmethod


class Exporter(ABC):
    """Base class for exporter

    Args:
        ABC (_type_): _description_
    """

    @abstractmethod
    def prepare_export(self):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self):
        """Exports the video data to a folder."""


class VideoExporter(Exporter):
    """Video Exporter

    Args:
        Exporter (_type_): Inherits exporter
    """

    def prepare_export(self):
        print("Prepares video data for exporting ")

    def do_export(self):
        print("Exports the video data to a folder ")


class AudioExporter(Exporter):
    """Audio Exporter

    Args:
        Exporter (_type_): Inherits exporter
    """

    def prepare_export(self):
        print("Prepares audio data for exporting ")

    def do_export(self):
        print("Exports the audio data to a folder ")


EXPORTERS = {"video": VideoExporter(), "audio": AudioExporter()}


def read_exporter() -> Exporter:
    """Constructs an exporter factory based on the user's preference.

    Returns:
        ExporterFactory: _description_
    """
    while True:
        export_type = input("enter the exporter: ")
        try:
            return EXPORTERS[export_type]
        except KeyError as e:
            print(f"Unknown exporter type {export_type}")


def do_export(exporter: Exporter) -> None:
    exporter.prepare_export()
    exporter.do_export()


if __name__ == "__main__":
    exporter = read_exporter()
    do_export(exporter=exporter)
