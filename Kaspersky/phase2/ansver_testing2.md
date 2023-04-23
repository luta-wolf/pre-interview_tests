### Test case #1: Upload a file for scanning

STEPS:

| #  | Action | Expected value |
| :-: | :----- | :-------: |
| 1	  | Upload a file using API endpoint. | Successful response with HTTP status code 200. |
| 2	  | Check if the file is being analyzed. | The API response should indicate that the file is being analyzed. |
| 3	  | Retrieve the analysis report for the file. | Successful response with HTTP status code 200 and the analysis report containing threat score and relevant context.|

### Test case #2: Get a file report by hash

STEPS:

| # | Action | Expected value |
| :-: | :----- | :-------: |
| 1 | Obtain the hash of a file. | The file hash should be valid. |
| 2 | Use the hash to get the analysis report for the file. | Successful response with HTTP status code 200 and the analysis report containing threat score and relevant context. |

### Test case #3: Scan URL

STEPS:

| # | Action | Expected value |
| :-: | :----- | :-------: |
| 1 | Scan a URL using the API endpoint. | Successful response with HTTP status code 200. |
| 2 | Check if the URL is being analyzed. | The API response should indicate that the URL is being analyzed. |
| 3 | Retrieve the analysis report for the URL. | Successful response with HTTP status code 200 and the analysis report containing threat score and relevant context. |

### Test case #4: Get a URL analysis report

STEPS:

| # | Action | Expected value |
| :-: | :----- | :-------: |
| 1 | Obtain a valid URL. | The URL should be valid. |
| 2 | Use the URL to get the analysis report. | Successful response with HTTP status code 200 and the analysis report containing threat score and relevant context. |

### Test case #5: Get a domain report

STEPS:

| # | Action | Expected value |
| :-: | :----- | :-------: |
| 1 | Obtain a valid domain name. | The domain name should be valid. |
| 2 | Use the domain name to get the analysis report. | Successful response with HTTP status code 200 and the analysis report containing threat score and relevant context. |

### Test case #6: Get an IP address report

STEPS:

| # | Action | Expected value |
| :-: | :----- | :-------: |
| 1 | Obtain a valid IP address. | The IP address should be valid. |
| 2 | Use the IP address to get the analysis report. | Successful response with HTTP status code 200 and the analysis report containing threat score and relevant context. |

