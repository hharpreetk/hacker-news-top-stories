# Hacker News Top Stories Visualization

This Python script retrieves the top stories from Hacker News using the Hacker News API and creates a bar chart visualization using Plotly Express. It displays the top 30 stories based on their scores, along with author names, truncated titles, and the number of comments.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `plotly`

## Installation

1. Clone or download this repository.

   ```bash
   git clone https://github.com/hharpreetk/hacker-news-top-stories-data-viz.git
   cd hacker-news-top-stories-data-viz

2. Install the required packages.
   ```
   pip install requests pandas plotly
   ```

## Usage

1. Run the script hn_viz.py.

2. The script will retrieve the top stories from Hacker News and create an interactive bar chart visualization using Plotly Express.

3. Hover over the bars in the bar chart to see additional information about each story, including the full title, author, and number of comments.

## Customization

- You can modify the max_title_length variable in the script to control the maximum length of truncated titles in the visualization.
- Adjust the layout and styling of the visualization in the code to suit your preferences.

## Credits
- Hacker News API: Hacker News API
- Plotly Express: Plotly

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
