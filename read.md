# Project Name

To create a simple Flask API endpoint that performs a left join operation
on two dataframes. The input to this endpoint should be two dataframes in JSON
format, and the output should be the resulting dataframe from the join operation in
JSON format.

## Project Prerequisites

python 3.8 + version
Flask
pandas
json
joiner

## steps to set up

Follow these steps to set up and run the project locally:

1. Clone the repository: `git clone https://github.com/himani-pathak/Join-DataFrame.git`
2. Change to the project directory: `cd project_directory`
3. Install the required dependencies: `pip install -r requirements.txt`

## API Documentation

Set the request method to POST.
Set the request URL to http://127.0.0.1:5000/joinDataframes.
Set the request body to the JSON format described above.
status (string): The status of the API call, indicating success or error.
message (string): Additional message regarding to input validation or error message.
If there is success status API responds with the resulting joined dataframe in JSON format.

## Example Of Jason Body 
{
    "df1": {
      "Student_ID": [1001,1002],
      "Name": ["Hinal","Shivani"]
    },
    "df2": {
      "Student_ID": [1001,1003],
      "student_class": ["second","First"]
    },
    "joinType": "left",
    "joiningKeys": "Student_ID"
    
}


### API Endpoint

/joinDataframes



