from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type


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


@dataclass
class MediaExporter:
    video: VideoExporter
    audio: AudioExporter


@dataclass
class MediaExporterFactory:
    video_class: Type[VideoExporter]
    audo_class: Type[AudioExporter]

    def get_media_exporter(self) -> MediaExporter:
        return MediaExporter(video=self.video_class(), audio=self.audo_class())


FACTORIES = {
    "media": MediaExporterFactory(video_class=VideoExporter, audo_class=AudioExporter)
}


def read_exporter() -> MediaExporterFactory:
    """Constructs an exporter factory based on the user's preference.

    Returns:
        ExporterFactory: _description_
    """
    while True:
        export_type = input("enter the exporter: ")
        try:
            return FACTORIES[export_type]
        except KeyError:
            print(f"Unknown exporter type {export_type}")


def do_export(exporter: MediaExporter) -> None:
    audio_exporter = exporter.audio
    video_exporter = exporter.video
    audio_exporter.prepare_export()
    audio_exporter.do_export()
    video_exporter.prepare_export()
    video_exporter.do_export()


if __name__ == "__main__":
    media_exporter_factory: MediaExporterFactory = read_exporter()
    media_exporter: MediaExporter = media_exporter_factory.get_media_exporter()
    do_export(exporter=media_exporter)
