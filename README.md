Based on the provided data, evaluating only the aspect of speed when checking a series of SHA-256 strings, the TXT search is consistently faster than the JSON query. According to the data, the time it took to find the last string is as follows:

TXT Search Time: The time taken to find the last string is consistently lower across all sizes of input, ranging from 0.000186 seconds for 512 strings to 0.674676 seconds for 2,097,152 strings.

JSON Search Time: The JSON query is slower in comparison, taking 0.000829 seconds for 512 strings and 7.767487 seconds for 2,097,152 strings.

If concern over a false positive, the code could check the position the string starts at, which would invalidate any and all false positives


| Number of Strings | TXT Search Time (s) | JSON Search Time (s) |   Ratio   |
|-------------------|---------------------|----------------------|-----------|
| 512               | 0.000186            | 0.000829             | 4.4564    |
| 1024              | 0.000235            | 0.001090             | 4.6332    |
| 2048              | 0.000417            | 0.002108             | 5.0531    |
| 4096              | 0.000769            | 0.004898             | 6.3657    |
| 8192              | 0.001492            | 0.008732             | 5.8523    |
| 16384             | 0.002868            | 0.088190             | 30.7528   | # TXT has stable increase, while JSON has anomaly going from 0.008 to 0.08, whereas the expected was to go from 0.008 to 0.016
| 32768             | 0.005504            | 0.036880             | 6.7004    |
| 65536             | 0.010869            | 0.126118             | 11.6035   |
| 131072            | 0.027713            | 0.252027             | 9.0941    |
| 262144            | 0.051295            | 0.574504             | 11.2000   |
| 524288            | 0.160129            | 1.856699             | 11.5950   |
| 1048576           | 0.226638            | 2.606580             | 11.5011   |
| 2097152           | 0.674676            | 7.767487             | 11.5129   |

Conclusion: If the system needs to check a series of SHA-256 strings, performing a TXT search is faster than executing a JSON query. Moreover, the efficieny increases with more data unlike JSON which decreases leading to bloat. This can be done with any system of fixed length.
