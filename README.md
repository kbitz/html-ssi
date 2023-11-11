# html-ssi -- Server Side Includes for HTML Files

## Summary

This script is intended to provide simple server side includes to regular HTML files. I maintain a simple personal website, and wanted to have a sidebar + page analytics included in every page without hardcoding them. There are obviously many full-featured static site generators however all of them seemed overkill considering I just needed this single feature.

## Usage

Simply provide the source directory that contains your HTML files containing include statements, and the directory where you would like the resulting html files to be written. The include files should be inside the source directory in a folder called `_includes`.

The syntax for an include statment is `<!-- %include% file_to_include.html -->`. We are wrapping the statement in an HTML comment so that the files still present as valid HTML should you be using some kind of validation or linting tool.

## License

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/deed.en)
