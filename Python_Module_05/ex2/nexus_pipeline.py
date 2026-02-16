from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union, Protocol


class ProcessingStage(Protocol):
    """Protocol defining the interface for all processing stages."""
    def process(self, data: Any) -> Any:
        """Execute the stage's logic on provided data."""
        pass


class InputStage():
    """Converts various raw data formats into a structured dictionary."""
    def process(self, data: Any) -> Dict:
        """Parse raw input (dict, stream, or CSV) into a dictionary."""
        result: Dict = dict()
        if isinstance(data, dict):
            for key, value in data.items():
                result.update({key: value})
        elif isinstance(data, str) and "|" in data:
            data_splitted = data.split("|")
            for item in data_splitted:
                key, value = item.split(":", 1)
                result.update({key.strip(): value.strip()})
        elif "," in data:
            data_splitted = data.split(",")
            i = 0
            for i in range(0, len(data_splitted), 2):
                key = data_splitted[i]
                if i + 1 < len(data_splitted):
                    value = data_splitted[i + 1]
                else:
                    value = None
                result.update({key.strip(): value.strip()})
        return result


class TransformStage():
    """Performs data cleaning and numeric type conversion."""
    def process(self, data: Any) -> Dict:
        """Convert dictionary string values to floats where possible."""
        result: Dict = {}
        for key, value in data.items():
            try:
                result.update({key: float(value)})
            except ValueError:
                continue
        return result


class OutputStage():
    """Formats processed data into a final readable string report."""
    def process(self, data: Any) -> str:
        """Convert a dictionary into a formatted integration string."""
        result: List = []
        for key, value in data.items():
            result.append(f"{key}: {value}")
            str_result = ", ".join(result)
        return f"[INTEGRATED_DATA] >> {str_result}"


class ProcessingPipeline(ABC):
    """Abstract base class for creating modular data pipelines."""
    def __init__(self, pipeline_id: Any) -> None:
        """Initialize the pipeline with an ID and an empty stages list."""
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        """Append a new processing stage to the pipeline sequence."""
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Abstract method to define the pipeline execution logic."""
        pass


class JSONAdapter(ProcessingPipeline):
    """Pipeline specialized in handling JSON-formatted data structures."""
    def __init__(self, pipeline_id: Any) -> None:
        """Initialize JSONAdapter using the parent pipeline constructor."""
        super().__init__(pipeline_id)

    def process(self, data: Dict) -> Union[str, Any]:
        """Sequence data through all stages for JSON processing."""
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class CSVAdapter(ProcessingPipeline):
    """Pipeline specialized in handling comma-separated string data."""
    def __init__(self, pipeline_id: Any) -> None:
        """Initialize CSVAdapter using the parent pipeline constructor."""
        super().__init__(pipeline_id)

    def process(self, data: str) -> Union[str, Any]:
        """Sequence data through all stages for CSV processing."""
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class StreamAdapter(ProcessingPipeline):
    """Pipeline specialized in handling real-time pipe-separated streams."""
    def __init__(self, pipeline_id: Any) -> None:
        """Initialize StreamAdapter using the parent pipeline constructor."""
        super().__init__(pipeline_id)

    def process(self, data: str) -> Union[str, Any]:
        """Sequence data through all stages for stream processing."""
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class NexusManager:
    """Orchestrates multiple pipelines to process diverse data inputs."""
    def __init__(self) -> None:
        """Initialize NexusManager with an empty list of pipelines."""
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register a new pipeline to the manager's control list."""
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> None:
        """Execute all registered pipelines on the provided data input."""
        print(f"{'='*22} PROCESS COMPLETE {'='*22}\n")
        for pipeline in self.pipelines:
            result = pipeline.process(data)
            print(f"[{pipeline.__class__.__name__}] ID: \
{pipeline.pipeline_id} | Status: OK")
            print(f"   └── Result: {result}")
        print(f"{'='*22} PROCESS COMPLETE {'='*22}\n")


def main():
    """Main entry point to demonstrate the Nexus Integration system."""
    # data_stream = "ID:707|TEMP:36.6|STATUS:WARM"
    data_csv = "id, 505, price, 199.99, priority, high"
    # data_json = {"id": 303, "type": "Admin", "active": True}

    nexus = NexusManager()

    stream_pipe = StreamAdapter("STREAM_01")
    json_pipe = JSONAdapter("JSON_01")
    csv_pipe = CSVAdapter("CSV_01")

    input_step = InputStage()
    transform_step = TransformStage()
    output_step = OutputStage()

    stream_pipe.add_stage(input_step)
    stream_pipe.add_stage(transform_step)
    stream_pipe.add_stage(output_step)

    json_pipe.add_stage(input_step)
    json_pipe.add_stage(transform_step)
    json_pipe.add_stage(output_step)

    csv_pipe.add_stage(input_step)
    csv_pipe.add_stage(transform_step)
    csv_pipe.add_stage(output_step)

    nexus.add_pipeline(stream_pipe)
    nexus.add_pipeline(json_pipe)
    nexus.add_pipeline(csv_pipe)

    # nexus.process_data(data_stream)
    # nexus.process_data(data_json)
    nexus.process_data(data_csv)


if __name__ == "__main__":
    main()
