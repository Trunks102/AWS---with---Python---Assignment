with open("sample_text_file.txt", "w") as file:
    # Write some paragraphs to the file
    paragraphs = [
       "The knockout tournament, featuring 128 skilled players," 
       "will undergo a series of intense matches to determine the ultimate champion." 
       "In each game, winners advance and losers are eliminated," 
       "gradually narrowing down the competition." 
       "Through seven thrilling rounds, the field will be winnowed down until only one player remains," 
       "claiming the coveted title of tournament winner." 
       "With 127 games required to crown the champion," 
       "the stakes are high and every match counts."
    ]
    
    for paragraph in paragraphs:
        file.write(paragraph + "\n\n")

print("Paragraphs have been written to the file.")