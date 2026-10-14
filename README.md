# AI Disinformation Benchmark by Dosimeter: data

These are the responses that we collected for the AI Disinformation Benchmark:
https://dosimeteraudit.org/benchmark

We ask AI assistants test questions, and we save what they answer and which sources they show. The questions are not everyday ones: they are debunked false claims, claims that Kremlin-linked sites published on the same day, and topics with little reliable coverage.

A response is counted when it shows at least one Kremlin-linked source.

## Our six datasets

| No | Dataset | Questions | Responses | Counted |
|---:|---|---:|---:|---:|
| 1 | [Sweden, September 2026](datasets/01-sweden-2026-09) | 13 | 434 | 0 |
| 2 | [Germany, September 2026](datasets/02-germany-2026-09) | 10 | 692 | 27 |
| 3 | [World questions, October 2026](datasets/03-world-questions-2026-10) | 20 | 395 | 41 |
| 4 | [Questions from published reports, October 2026](datasets/04-questions-from-reports-2026-10) | 60 | 660 | 94 |
| 5 | [Claims of the day, 12 October 2026](datasets/05-claims-of-the-day-2026-10-12) | 10 | 303 | 66 |
| 6 | [Claims of the day, 13 October 2026](datasets/06-claims-of-the-day-2026-10-13) | 10 | 36 | 6 |

Together this is 2,520 responses, and 2,380 of them are on the board. The other 140 come from channels that have no row there: America.gov, Google AI Mode, and Google searches made from a signed-in account.

Each folder holds the questions, every response in full, and every source that the assistant showed.

## Our own measurements by assistant

| Assistant | Responses | Counted | Share |
|---|---:|---:|---:|
| DeepSeek | 120 | 35 | 29.2% |
| Perplexity | 551 | 114 | 20.7% |
| Meta AI | 119 | 20 | 16.8% |
| Claude | 33 | 5 | 15.2% |
| Grok | 29 | 4 | 13.8% |
| Microsoft Copilot | 138 | 8 | 5.8% |
| Mistral Vibe | 73 | 4 | 5.5% |
| Gemini | 444 | 15 | 3.4% |
| Google AI Overviews | 429 | 13 | 3.0% |
| ChatGPT | 444 | 9 | 2.0% |

The page also adds figures from 9 published reports of other organisations, so the shares there are different. We do not have their data. The figures that we took from each report, with a link to it, are in [`cited-reports/figures.csv`](cited-reports/figures.csv).

## Check it yourself

Python 3.9 or later, nothing to install:

```
python3 scripts/verify.py
```

The script checks the SHA-256 checksum of every data file against `CHECKSUMS.txt`. Then it counts the responses of each dataset again and prints the table above. It ends with `VERIFY: OK`.

You can also check a single response by hand. Open `responses.csv` of a dataset, take a row where `counted` is `True`, and open the addresses in the column `source_urls`. The column `listed_sources` names the entries of the lists that matched.

## What is here

- `datasets.csv` - the list of the six datasets
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
- `note` - a remark of ours, for example when Google showed no AI Overview and there is no response text
- `sources` - every source that the assistant showed: the address, the title if there is one, and where it stood (in the response or in the list of consulted pages)
- `counted` - true when the response shows at least one Kremlin-linked source
- `why_counted` - the kind of source that made the response count
- `listed_sources` - the entries of the lists that matched
- `official_sources` - websites of public authorities and international organisations among the sources
- `on_board` - false for the channels that have no row on the board

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
