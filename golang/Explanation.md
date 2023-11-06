# Hello

Dear Tomas,

I sincerely apologize for not completing the assignment in Golang as I originally hoped. Due to unexpected commitments and time constraints, I had to make the difficult decision to implement solely in Python, despite my genuine enthusiasm for improving with and using Golang. Please understand that this decision was not taken lightly, and I deepy regret irony of applying for a Golang oriented position with a Python submission. My primary goal was to ensure the assignment's timely completion, and I am fully committed to delivering the best results possible within the given circumstances.

Thank you for your understanding and consideration.

Warm regards,
Aaron R. 


## Rough Mockup of Go

This is an incomplete codesnippet of how I would've approached the random quote solution in golang. 

As explained above, I switched back to Python a language I am far more comfortable in, in order to complete the task swiftly. 

```golang

func getQuote() {
	quoteAPI := "http://api.forismatic.com/api/1.0/"
	key := "" 
	keyQuery := "" 

	// Create HTTP client
	client := &http.Client{}

	// quote_url for the GET request
	quote_url := fmt.Sprintf("%s?method=getQuote&lang=en&format=json%s", quoteAPI, keyQuery)

	// Send GET request
	resp, err := client.Get(quote_url)
	if err != nil {
		fmt.Printf("An error occurred while making the request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Check status code
	if resp.StatusCode != http.StatusOK {
		fmt.Printf("Received a non-OK status code: %v\n", resp.Status)
		return
	}

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("An error occurred while reading the response body: %v\n", err)
		return
	}

	// Parse response
	var quoteData map[string]interface{}
	if err := json.Unmarshal(body, &quoteData); err != nil {
		fmt.Printf("An error occurred while parsing the JSON response: %v\n", err)
		return
	}

	// Extract the quoteText
	quoteText, ok := quoteData["quoteText"].(string)
	if !ok {
		fmt.Println("Failed to extract the quoteText")
		return
	}

	// Print the quote
	fmt.Printf("Random Quote: %s\n", quoteText)
}
```