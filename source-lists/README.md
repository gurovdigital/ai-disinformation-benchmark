# Which sites count as Kremlin-linked

`counted-sites.csv` lists every site that made at least one response count in our measurements, and the number of responses that show it.

The column `counted_as` has three values:

- site on the lists: the site is on the European Union sanctions list (Council Regulation 833/2014, Annex XV) or on a list of the Pravda network (VIGINUM, CheckFirst). The copies of these lists that we froze for the Germany measurement are in https://github.com/gurovdigital/election-day-ai-poisoning-germany-2026/tree/main/germany-2026/lists
- Kremlin state body or state media
- pro-Kremlin outlet or mirror site

For the second and the third kind the file says what the site is and gives a published proof: who named it, and the sentence from that page. We read every quote again on its page on 14 October 2026.

Some proofs name the organisation itself, and some name its owner, its founder or its editor. The column `proof_covers` says which.
