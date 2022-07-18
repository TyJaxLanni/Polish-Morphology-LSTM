
#!/usr/bin/env python

import argparse


def prepareFiles(input_path: str, gen_path: str, nom_path: str) -> None:
    # open input file
    with open(input_path, "r", encoding='utf-8') as fInput, open(gen_path, "w", encoding='utf-8') as gOutput, open(nom_path, "w", encoding='utf-8') as nOutput:
        # for each line in the input, split the first word into the nom file (with spaces) and the rest to the gen file
        for line in fInput:

            print("-----------------")

            nom_word = line.split()[0]
            gen_word = line.split()[1]
            word_with_space = ""

            for c in nom_word:

                word_with_space += c.casefold() + " "
                    
                # so I can see on the console
                   
                print("nom: ", word_with_space.strip())
                print(word_with_space.strip(), file=nOutput)

            word_with_space = ""

            for c in gen_word:

                word_with_space += c.casefold() + " "
                        
                 # so I can see on the console
                    
                print("genitive: ", word_with_space.strip())                    
                print(word_with_space.strip(), file=gOutput)


def main(args: argparse.Namespace) -> None:

    prepareFiles(args.input_file, args.gen_file, args.nom_file)
    print("Finished!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str,
                        help="file for our program to read")
    parser.add_argument("nom_file", type=str,
                        help="output file for nom")
    parser.add_argument("gen_file", type=str,
                        help="output file for genitive")
    args = parser.parse_args()
    main(args)
