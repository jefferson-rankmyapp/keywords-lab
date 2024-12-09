import json

def generate_report(results, filename="report.json"):
    try:
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
        return f"Relatório salvo como {filename}"
    except Exception as e:
        return f"Erro ao salvar o relatório: {e}"
