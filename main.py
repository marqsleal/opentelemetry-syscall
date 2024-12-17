from sys import stdout
import argparse
from time import time

#OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter


def configure_tracer(service_name: str) -> int:
    resource = Resource.create({"service.name": service_name})

    trace.set_tracer_provider(
        TracerProvider(resource=resource)
    )

    tracer_provider = trace.get_tracer_provider()

    otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

    span_processor = SimpleSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)

    return 0

def for_print(n_rep: int) -> int:
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span('for_print'):
        for n in range(n_rep):
            print(f'{n}')

    return 0

def for_write(n_rep: int) -> int:
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span('for_write'):
        for n in range(n_rep):
            stdout.write(f'{n}\n')

    return 0

def main() -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'funcao',
        choices=['print', 'write'],
        help="Escolha entre 'print' ou 'write' para execução."
    )

    parser.add_argument(
        '--range', 
        type=int, 
        default=1 << 20,
        help="Escolha um número máximo de repetições (Padrão: 1048576)."
    )

    args = parser.parse_args()

    configure_tracer(service_name=f'func: {args.funcao} - range: {args.range}')

    if args.funcao == 'print':
        for_print(args.range)
    elif args.funcao == 'write':
        for_write(args.range)

    return 0
    

if __name__ == '__main__':
    main()