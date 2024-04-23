from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/get')
def get_request_data():
    # Get all query parameters from the request URL
    query_params = request.headers

    # Start building HTML response
    html_response = "<html><body><h1>Request Data:</h1><ul>"

    # Iterate over query parameters and add them to HTML response
    for key, value in query_params:
        html_response += f"<li>{key}: {value}</li>"

    # Close HTML response
    html_response += "</ul></body></html>"

    # Return HTML response
    return html_response, 200

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(debug=True)
