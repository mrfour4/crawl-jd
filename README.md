# Job Crawler for ITviec & VietnamWorks

This project provides a Python-based job crawler that extracts recruitment data from two major platforms: [ITviec](https://itviec.com) and [VietnamWorks](https://vietnamworks.com). All crawled data is stored in MongoDB.

---

## 💾 Requirements

### 1. Python & Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Environment Variables

Create a `.env` file in the root directory by copying the provided example:

```bash
cp .env.example .env
```

Then fill in the following fields in `.env`:

```env
MONGO_URI=your_mongo_connection_string
MONGO_DB=crawl-data
MONGO_COLLECTION=jd
```

---

## 🚀 Running the Crawlers

### 1. Crawl ITviec data

```bash
xvfb-run -a python ./src/itviec_crawl.py
```

### 2. Crawl VietnamWorks data

```bash
xvfb-run -a python ./src/vietnamwork_crawl.py
```

---

## 🔁 Resume Crawling from a Specific Page

If the crawler is interrupted or fails at a specific page, resume from that page using the `--start-page` option.

### Resume ITviec from page 2:

```bash
xvfb-run -a python ./src/itviec_crawl.py --start-page 2
```

### Resume VietnamWorks from page 2:

```bash
xvfb-run -a python ./src/vietnamwork_crawl.py --start-page 2
```

> ⚠️ Note: `--start-page` is 1-based (i.e., page number as shown in the browser), not API-indexed.

---

## 🧾 MongoDB Data Structure

- **Database**: as specified in `MONGO_DB`
- **Collection**: as specified in `MONGO_COLLECTION`
- **Unique Key**: `hash`

---

## 📁 Project Structure

```
crawl-jd/
├── .env.example
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── itviec_crawl.py
│   ├── vietnamwork_crawl.py
│   └── mongo_config.py
└── ...
```

---

## 📌 Notes

- `xvfb-run` is used to run headless browsers on systems without a graphical interface (e.g., Linux servers).
- The script automatically **skips duplicates** using the `hash` field as a unique identifier.

