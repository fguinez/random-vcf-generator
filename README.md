# Random CVF Generator
A tool written in Python to generate vcf files with random data, useful for testing applications.

Files with the `.vcf` extension are useful for quickly creating multiple contacts on cell phones. This tool seeks to help populate your development demos by randomly generating a file with the desired number of contacts.

## Use

```
python main.py [prefix] [number_of_contacts] [start_number]
```
- `[prefix]`: Common prefix to all contact names to create
- `[number_of_contacts]`: Number of contacts to contain within the file
- `[start_number]`: Within the names of the contacts, the number from which it starts to identify them 1 by 1

## To-Do list

- Use a template as a basis to guide the format of the generation of each contact.
- Custom file names
- Realistic randomly generated usernames option 
- Optional parameters to add prefix, suffix, or identifying number to contact names
