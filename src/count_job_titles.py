from collections import Counter
import json
from mongo_config import collection

def count_job_titles_fallback(output_file="job_title_counts.json"):
    cursor = collection.find({}, {"job_title": 1})  # Lấy mỗi trường job_title

    counter = Counter()
    for doc in cursor:
        job_title = doc.get("job_title")
        if job_title:
            counter[job_title] += 1

    result = [{"job_title": title, "count": count} for title, count in counter.most_common()]

    with open(output_file, mode='w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Job title frequencies written to {output_file}")

if __name__ == "__main__":
    count_job_titles_fallback()
