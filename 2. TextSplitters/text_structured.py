from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """As a student, much of your time will be spent interacting with texts of all types, shapes, sizes, and delivery methods.

In academic terms, a text is anything that conveys a set of meanings to the person who examines it. You might have thought that texts were limited to written materials, such as books, magazines, newspapers, and ‘zines (an informal term for magazine that refers especially to fanzines and webzines). Those items are indeed texts—but so are movies, paintings, television shows, songs, political cartoons, online materials, advertisements, maps, works of art, and even rooms full of people. If we can look at something, explore it, find layers of meaning in it, and draw information and conclusions from it, we’re looking at a text.
Most of the texts you’re exposed to in your academic career will be print (on paper/hard copy) or online written texts like books, articles, and essays—these are still the most common types of learning material.

Text Attributions
This chapter was adapted from “What is a Text” in The Word on College Reading and Writing by Carol Burnell, Jaime Wood, Monique Babin, Susan Pesznecker, and Nicole Rosevear, which is licensed under a CC BY-NC 4.0 Licence. Adapted by Allison Kilgannon.
"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300, 
    chunk_overlap=0
)

chunks = splitter.split_text(text) 

print( len(chunks))

print( chunks)

#we will mostly use text structured for splitting the text 
# it's chunk size will matter on the bases of the text we are giving it's effiecient and doesn't break the words in half