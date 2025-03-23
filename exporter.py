import os

def export_results_to_file(results: dict, ticker: str, folder: str = "results"):
    """
    Exports the analysis results to a text file in a specified folder.

    Parameters:
        results (dict): A dictionary of stock analysis results.
        ticker (str): The stock ticker symbol (used in the filename).
        folder (str): Directory to save the file (default is 'results').
    """

    # Create the folder if it doesn't already exist
    os.makedirs(folder, exist_ok=True)

    # Construct the file path inside the results folder
    filename = os.path.join(folder, f"{ticker}_analysis.txt")

    try:
        # Open the file for writing and write the analysis results
        with open(filename, "w") as file:
            # Optional header for readability
            file.write(f"{ticker} Stock Analysis Results\n")
            file.write("=" * 40 + "\n")
            for key, value in results.items():
                # Format key names nicely and write each result
                file.write(f"{key.replace('_', ' ').capitalize()}: {value}\n")

        print(f"\nResults saved to {filename}")
    except Exception as e:
        # If there's an error, show it in the console
        print(f"Failed to save results: {e}")