# ANONO - URL Decluttering Tool


ANONIX is a Python tool designed to declutter URL lists for crawling and penetration testing. This tool is easy to use and does not require a username or password for installation.

## Features

- **Declutter URLs**: Remove unnecessary parts from URLs to make them more manageable.
- **Simple Command-Line Interface**: User-friendly interface for easy interaction.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hackinter/anono.git
   cd anono
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Tool**:
   Execute the following command to start using ANONIX:
   ```bash
   python -m anono
   ```

## Usage

1. **Input URLs**: When prompted, enter the URLs you want to declutter. You can enter one URL per line.
2. **View Results**: After processing, the cleaned URLs will be displayed in the terminal.

### Example

```bash
Enter URLs to declutter (type 'exit' to quit):
http://example.com/page?param=value&other=1
https://www.example.com?utm_source=google
exit
```

The output will be the cleaned URLs without unnecessary parameters.

## Guidelines for Use

- **Ethical Usage**: Ensure that you have permission to process the URLs you are decluttering. Unauthorized scanning or crawling can be illegal and unethical.
- **Respect Robots.txt**: Always check the `robots.txt` file of the website to ensure you are allowed to access its pages.
- **Limit Requests**: Avoid sending too many requests in a short period, as this may overload the server and lead to IP blocking.

## Customization

You can easily customize the tool by modifying the source code according to your needs. Here are some aspects you can customize:

- **Input and Output Format**: Change how the tool reads input URLs and how it outputs the cleaned URLs.
- **Additional Features**: Add more functionality, like saving the cleaned URLs to a file or supporting more URL formats.

## Contributions

Feel free to contribute to the project! You can open issues for bugs, feature requests, or improvements.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for more details.




Thank you for using ANONIX!
```

This version includes a detailed usage section along with guidelines for ethical use. Let me know if you need any more modifications!
