// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})

// Task 4: update to add birthday
db.authors.updateOne({"name": "Jane Austen"}, {$set: {"birthday": "1775-12-17"}})

// Task 5: insert four more authors
db.authors.insertOne({
  "name": "J. K. Rowling",
  "nationality": "British",
  "bio": {
    "short": "Wrote Harry Potter books.",
    "long": "Rowling is a British author who is known for writing the Harry Potter Books."
  },
"Birthday": "1965-07-35"
})

db.authors.insertOne({
  "name": "Stephen King",
  "nationality": "American",
  "bio": {
    "short": "Writes horror books.",
    "long": "King has published over 67 novels and is known for writing in the horror genre."
  },
"Birthday": "1947-09-21"
})

db.authors.insertOne({
  "name": "Franz Kafka",
  "nationality": "Czech",
  "bio": {
    "short": "Wrote short stories.",
    "long": "Kafka was known for his short stories, blending themes of modernism, existentialism, and surrealism."
  },
"Birthday": "1883-07-03"
})

db.authors.insertOne({
  "name": "Leo Tolstoy",
  "nationality": "Russian",
  "bio": {
    "short": "Was an author and moral philosopher",
    "long": "Tolstoy wrote realistic fiction exploring Russian society and morality"
  },
"Birthday": "1828-09-09"
})

// Task 6: total count
db.authors.countDocuments()

// Task 7: British authors, sorted by name
db.authors.find({"nationality": "British"}).sort({"name": 1})

