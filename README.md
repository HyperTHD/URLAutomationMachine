# URLAutomationMachine

The machine we all need but the one we most likely do not deserve. The url checking program we all desire

![UrlAutomationMachine](/resources/urlAutomationMachine.png)

Install this tool by using the following command:

```pip install UrlAutomationMachine```

Running this tool from your command line can be done as simply as specifying the name followed by the argument you wish to use

```$ UrlAutomationMachine -f [filename]```

## Features

- Uses regex to parse each line for a url
- Processes each request and checks status code for successful attempt
- Any url with a status code around ```200``` will pass automation. Shown with a green color
- Urls with a status code of ```404``` or ```400``` will fail automation. Shown with a red color
- Urls with a status code that is unknown ```403``` will fail automation. Shown with a grey color

## Options

|Arguments | Description |
|-----------------|--------------|
| -f [file] | Reads urls from a given file to process |
| -u [url] | Processes the specified url |
| -j | Output will be displayed in a JSON format |
| -i [file] | Reads urls from a given file to ignore |
| -t | Check the status of the latest 10 Telescope posts |

## Contributing

I welcome any and all contributions to this project. Please make sure to follow the instructions in the contributing
file in order to effectively develop on this project.
You can read more [here](CONTRIBUTING)

## Licensing

This project is distributed under the MIT License which can be found [here](LICENSE)
