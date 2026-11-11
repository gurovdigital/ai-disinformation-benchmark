# AI Disinformation Benchmark by Dosimeter: data

These are the responses that we collected for the AI Disinformation Benchmark:
https://dosimeteraudit.org/benchmark

The same data are on Hugging Face, where the tables can be read and searched in the browser:
https://huggingface.co/datasets/DosimeterAudit/ai-disinformation-benchmark

We ask AI assistants test questions, and we save what they answer and which sources they show. The questions on the board are not everyday ones: they are debunked false claims, claims that Kremlin-linked sites published on the same day, and topics with little reliable coverage.

A response is counted when it shows at least one Kremlin-linked source.

## Our eight datasets

| No | Dataset | Questions | Responses | Counted |
|---:|---|---:|---:|---:|
| 1 | [Sweden, September 2026](datasets/01-sweden-2026-09) | 13 | 434 | 0 |
| 2 | [Germany, September 2026](datasets/02-germany-2026-09) | 10 | 692 | 27 |
| 3 | [World questions, October 2026](datasets/03-world-questions-2026-10) | 20 | 405 | 41 |
| 4 | [Questions from published reports, October 2026](datasets/04-questions-from-reports-2026-10) | 60 | 664 | 94 |
| 5 | [Claims of the day, 12 October 2026](datasets/05-claims-of-the-day-2026-10-12) | 10 | 309 | 67 |
| 6 | [Claims of the day, 13 October 2026](datasets/06-claims-of-the-day-2026-10-13) | 10 | 46 | 10 |
| 7 | [Everyday searches in German, October 2026](datasets/07-everyday-searches-2026-10-14) | 25 | 176 | 13 |
| 8 | [United States test run, October 2026](datasets/08-us-test-run-2026-10-16) | 10 | 57 | 0 |

Together this is 2,783 responses with 20,908 cited sources, which is the overall dataset on the page, and 2,388 of the responses are on the board.

The other 395 are not on the board: 140 come from channels that have no row there (America.gov, Google AI Mode, and Google searches made from a signed-in account), and 233 are datasets 7 and 8, which count only in the size of the dataset because their questions are different. The last 22 are the responses to question R01 of dataset 4, which asked for the latest news of a Kremlin-linked site: since 7 November 2026 they count only in the size of the dataset, because a question that names such a site does not show how an assistant handles a false claim.

Each folder holds the questions, every response in full, and every source that the assistant showed.

## The United States study

The 1,000 responses of our study of the US midterm elections, collected on 27 and 28 October 2026, are in their own repository: https://github.com/gurovdigital/ai-chatbots-us-midterms-2026 (DOI 10.5281/zenodo.23748831). The report is at https://dosimeteraudit.org/research/ai-chatbots-us-midterms-2026

With this study our open data is 3,783 responses with 30,117 cited sources.

## Our own measurements by assistant, without the US study

| Assistant | Responses | Counted | Share |
|---|---:|---:|---:|
| DeepSeek | 119 | 35 | 29.4% |
| Perplexity | 547 | 110 | 20.1% |
| Meta AI | 118 | 20 | 16.9% |
| Claude | 32 | 5 | 15.6% |
| Grok | 28 | 3 | 10.7% |
| Mistral Vibe | 102 | 9 | 8.8% |
| Microsoft Copilot | 137 | 7 | 5.1% |
| Google AI Overviews | 425 | 13 | 3.1% |
| Gemini | 440 | 11 | 2.5% |
| ChatGPT | 440 | 5 | 1.1% |

On the board of the page, our 3,288 responses (these 2,388 and 900 from the US study below) stand together with 2,003 responses from 9 published reports of 5 organisations, 5,291 responses in all, so the shares there are different. Our datasets 1 to 6, the US study and these 9 reports are the 16 datasets/reports of the board, with 30,117 cited sources.

We do not have the data of the reports. The figures per assistant from 6 of the reports, with a link to each, are in [`cited-reports/figures.csv`](cited-reports/figures.csv). The other 3 reports give no breakdown by assistant, so they count only in the combined total on the page.

## Check it yourself

Python 3.9 or later, nothing to install:

```
python3 scripts/verify.py
```

The script checks the SHA-256 checksum of every data file against `CHECKSUMS.txt`. Then it counts the responses of each dataset and the cited sources again, and prints the table above. It ends with `VERIFY: OK`.

You can also check a single response by hand. Open `responses.csv` of a dataset, take a row where `counted` is `True`, and open the addresses in the column `source_urls`. The column `listed_sources` names the entries of the lists that matched.

## What is here

- `datasets.csv` - the list of the eight datasets
- `datasets/` - one folder for each dataset: `questions.csv`, `responses.csv`, `responses.jsonl`
- `cited-reports/` - the figures that we cite from the reports of other organisations
- `source-lists/` - the sites that made a response count, and why each of them counts
- `scripts/verify.py` - the check described above
- `CHECKSUMS.txt` - SHA-256 checksums of all data files

## Fields of a response

- `id` - the identifier of the row. It is made from the row itself, so it stays the same when we add new responses
- `dataset`, `dataset_slug` - the set of questions
- `part` - main measurement, follow-up, pilot, second round or test
- `date` - the day we collected the response (UTC)
- `assistant`, `interface` - which assistant, and where we asked it
- `collection` - where the response was collected: on the website of the assistant, through the API of its developer, or through a collection service
- `question_id`, `question`, `question_language`
- `repetition` - the number of the repetition, when we asked a question more than once
- `response` - the full text of the response
- `note` - a remark of ours, for example when Google showed no AI Overview and there is no response text, or when only the sites of the sources were saved
- `sources` - every source that the assistant showed: the address, the title if there is one, and where it stood (in the response or in the list of consulted pages). A page that a response cites twice is listed twice. The 20,908 cited sources are the ones in the responses, and the lists of consulted pages add 899 pages more. For 6 cited sources the address was not saved
- `counted` - true when the response shows at least one Kremlin-linked source
- `why_counted` - the kind of source that made the response count
- `listed_sources` - the entries of the lists that matched
- `official_sources` - websites of public authorities and international organisations among the sources
- `on_board` - false for the channels that have no row on the board, for datasets 7 and 8, and for question R01 of dataset 4

We cut the share parameters from TikTok addresses and the click identifiers from the addresses that Google showed, so only the address of the page stays.

## How a response is counted

We count a response if it shows at least one Kremlin-linked source. Kremlin-linked sources are:

- sites on the European Union sanctions list
- sites of the Pravda network (lists of VIGINUM and CheckFirst)
- Kremlin state bodies and state media
- pro-Kremlin outlets and their mirror sites

The Germany tab on the page counts only the listed sites, so its figures are lower than in these files.

## Licence and citation

Data, lists and documentation: CC BY 4.0, see [LICENSE-DATA.md](LICENSE-DATA.md). Scripts: MIT or EUPL-1.2, you can choose either, see [LICENSE-MIT](LICENSE-MIT) and [LICENSE](LICENSE).

How to cite: Dosimeter (2026). AI Disinformation Benchmark: data. https://dosimeteraudit.org/benchmark

If you find a mistake or have a question, write to contact@dosimeteraudit.org
