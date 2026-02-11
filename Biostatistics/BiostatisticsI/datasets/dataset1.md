## Base Mouse Dataset

We consider 12 mice from three strains (B6, BALB, CAST) on two diets (Chow vs High-fat diet, HFD). For each mouse we record initial and 12-week weight, 12-week fasting glucose, activity score, and expression of two genes (Pparg and Il6). Hyperglycemia is defined as Glucose12 ≥ 140 mg/dL. The following are simulated, but plausible measurements:
•	Weight0 / Weight12: HFD animals gain more weight than Chow across strains.
•	Glucose12: HFD animals have higher glucose than Chow across strains.
•	Activity: Chow are generally less active than HFD in this toy experiment (you can blame enriched housing or running wheels for HFD if you want to justify it in words).
•	Pparg: higher with more weight gain.
•	Il6: higher with higher glucose (inflammation-ish).
•	Hyperglycemia: based on a relatively high glucose threshold; mostly HFD, one CAST HFD “protected” to keep some heterogeneity

|ID	|Strain|Diet|	Sex| Weight0|	Weight12|	Glucose12|	Activity |	Pparg	|I16|	Hyperglycemia|
|---|---|---|---|---|---|---|---|---|---|---|
|M1 |	B6| Chow |M	| 20| 22 | 118 |3.0	| 6	|4 |No|
|M2	| B6| Chow |F	| 19| 21|116 |3.5 |6 |4	|No|
|M3	| B6| HFD	|M| 20| 27| 162| 6.0| 8 | 7 | Yes|
|M4	| B6| HFD	|F| 19| 26| 160	| 6.5	| 8	|7	|Yes|
|M5	| BALB| Chow|	M |19 |21 |114 |4.0	|6 |4	|No|
|M6	| BALB| Chow |F	|18	|20	|112| 4.5 |	6 |	3 |	No|
|M7	| BALB| HFD |	M	| 19 |25|158| 7.0 |	7|7 |Yes|
|M8	| BALB| HFD |	F| 18 |24 |156 |7.5 |7 |6 |Yes|
|M9	| CAST| Chow |M |18	|20| 110|	5.0|	6|	3|	No|
|M10| CAST| Chow |F	| 17|	19	|108|	5.5	|6	|3|	No|
|M11|	CAST| HFD |	M |	18|	24|	154|	8.0 |	7|6|	No|
|M12| CAST| HFD	| F	|17|	23|	152|	8.5|	7	|6|	No|
