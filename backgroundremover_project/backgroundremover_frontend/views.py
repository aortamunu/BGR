from django.shortcuts import render
from django.http import HttpResponse
# Import the subprocess module to call the BackgroundRemover command-line tool
import subprocess


def index(request):
    if request.method == 'POST':
        # Handle file upload and background removal process here
        # Make sure to handle user inputs, file uploads, and call the BackgroundRemover tool

        # For example, you can get the uploaded file from the POST request
        uploaded_file = request.FILES['uploaded_file']

        # Define the command to call the BackgroundRemover tool with appropriate options
        # Replace '/path/to/backgroundremover' with the actual path to the command-line tool
        command = f'/path/to/backgroundremover -i {uploaded_file} -o output.png'

        # Use subprocess to run the command and remove the background
        try:
            subprocess.run(command, shell=True, check=True)
            # The above line will run the command and wait for it to finish before continuing
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"Error occurred: {str(e)}", status=500)

        # If the background removal was successful, you can send the processed image as a response
        # In this example, we'll just return a simple success message
        return HttpResponse("Background removed successfully!")

    return render(request, 'backgroundremover_frontend/index.html')
