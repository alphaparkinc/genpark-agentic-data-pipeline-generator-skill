from client import AgenticDataPipelineGeneratorClient

def main():
    client = AgenticDataPipelineGeneratorClient()
    res = client.build_pipeline("PostgreSQL", "Snowflake", ["strip_pii", "convert_currency_usd"])
    print(f"Status: {res['pipeline_status']}")
    print(f"Config: {res['pipeline_config']}")

if __name__ == "__main__":
    main()
