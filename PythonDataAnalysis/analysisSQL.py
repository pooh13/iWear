# ---分析貼文風格用SQL---

allSearchSQLCmd = ("SELECT * FROM post"+" "+
                  "WHERE (post.styleNo IN (SELECT styleNo FROM postcount INTERSECT SELECT styleNo FROM post))"+" "+
                  "AND (post.clothesNo IN (SELECT clothesNo FROM postcount INTERSECT SELECT clothesNo FROM post))"+" "+
                  "AND (post.coatNo IN (SELECT coatNo FROM postcount INTERSECT SELECT coatNo FROM post))"+" "+
                  "AND (post.pantsNo IN (SELECT pantsNo FROM postcount INTERSECT SELECT pantsNo FROM post))"+" "+
                  "AND (post.shoesNo IN (SELECT shoesNo FROM postcount INTERSECT SELECT shoesNo FROM post))"+" "+
                  "AND (post.accessoriesNo IN (SELECT accessoriesNo FROM postcount INTERSECT SELECT accessoriesNo FROM post))")

# all
# ------------------------------------------------------------------------------------------------------------------------------------------------

orACSearchSQLCmd = ("SELECT * FROM post"+" "+
                  "WHERE (post.styleNo IN (SELECT styleNo FROM postcount INTERSECT SELECT styleNo FROM post))"+" "+
                  "AND (post.clothesNo IN (SELECT clothesNo FROM postcount INTERSECT SELECT clothesNo FROM post))"+" "+
                  "AND (post.coatNo IN (SELECT coatNo FROM postcount INTERSECT SELECT coatNo FROM post))"+" "+
                  "AND (post.pantsNo IN (SELECT pantsNo FROM postcount INTERSECT SELECT pantsNo FROM post))"+" "+
                  "AND (post.shoesNo IN (SELECT shoesNo FROM postcount INTERSECT SELECT shoesNo FROM post))"+" "+
                  "OR (post.accessoriesNo IN (SELECT accessoriesNo FROM postcount INTERSECT SELECT accessoriesNo FROM post))")

orCOSearchSQLCmd = ("SELECT * FROM post"+" "+
                  "WHERE (post.styleNo IN (SELECT styleNo FROM postcount INTERSECT SELECT styleNo FROM post))"+" "+
                  "AND (post.clothesNo IN (SELECT clothesNo FROM postcount INTERSECT SELECT clothesNo FROM post))"+" "+
                  "OR (post.coatNo IN (SELECT coatNo FROM postcount INTERSECT SELECT coatNo FROM post))"+" "+
                  "AND (post.pantsNo IN (SELECT pantsNo FROM postcount INTERSECT SELECT pantsNo FROM post))"+" "+
                  "AND (post.shoesNo IN (SELECT shoesNo FROM postcount INTERSECT SELECT shoesNo FROM post))"+" "+
                  "AND (post.accessoriesNo IN (SELECT accessoriesNo FROM postcount INTERSECT SELECT accessoriesNo FROM post))")

orSHSearchSQLCmd = ("SELECT * FROM post"+" "+
                  "WHERE (post.styleNo IN (SELECT styleNo FROM postcount INTERSECT SELECT styleNo FROM post))"+" "+
                  "AND (post.clothesNo IN (SELECT clothesNo FROM postcount INTERSECT SELECT clothesNo FROM post))"+" "+
                  "AND (post.coatNo IN (SELECT coatNo FROM postcount INTERSECT SELECT coatNo FROM post))"+" "+
                  "AND (post.pantsNo IN (SELECT pantsNo FROM postcount INTERSECT SELECT pantsNo FROM post))"+" "+
                  "OR (post.shoesNo IN (SELECT shoesNo FROM postcount INTERSECT SELECT shoesNo FROM post))"+" "+
                  "AND (post.accessoriesNo IN (SELECT accessoriesNo FROM postcount INTERSECT SELECT accessoriesNo FROM post))")

orPASearchSQLCmd = ("SELECT * FROM post"+" "+
                  "WHERE (post.styleNo IN (SELECT styleNo FROM postcount INTERSECT SELECT styleNo FROM post))"+" "+
                  "AND (post.clothesNo IN (SELECT clothesNo FROM postcount INTERSECT SELECT clothesNo FROM post))"+" "+
                  "AND (post.coatNo IN (SELECT coatNo FROM postcount INTERSECT SELECT coatNo FROM post))"+" "+
                  "OR (post.pantsNo IN (SELECT pantsNo FROM postcount INTERSECT SELECT pantsNo FROM post))"+" "+
                  "AND (post.shoesNo IN (SELECT shoesNo FROM postcount INTERSECT SELECT shoesNo FROM post))"+" "+
                  "AND (post.accessoriesNo IN (SELECT accessoriesNo FROM postcount INTERSECT SELECT accessoriesNo FROM post))")

# orOne
# ------------------------------------------------------------------------------------------------------------------------------------------------

orACCOSearchSQLCmd = ("SELECT * FROM post"+" "+
                  "WHERE (post.styleNo IN (SELECT styleNo FROM postcount INTERSECT SELECT styleNo FROM post))"+" "+
                  "AND (post.clothesNo IN (SELECT clothesNo FROM postcount INTERSECT SELECT clothesNo FROM post))"+" "+
                  "OR (post.coatNo IN (SELECT coatNo FROM postcount INTERSECT SELECT coatNo FROM post))"+" "+
                  "AND (post.pantsNo IN (SELECT pantsNo FROM postcount INTERSECT SELECT pantsNo FROM post))"+" "+
                  "AND (post.shoesNo IN (SELECT shoesNo FROM postcount INTERSECT SELECT shoesNo FROM post))"+" "+
                  "OR (post.accessoriesNo IN (SELECT accessoriesNo FROM postcount INTERSECT SELECT accessoriesNo FROM post))")

orACCOSHSearchSQLCmd = ("SELECT * FROM post"+" "+
                  "WHERE (post.styleNo IN (SELECT styleNo FROM postcount INTERSECT SELECT styleNo FROM post))"+" "+
                  "AND (post.clothesNo IN (SELECT clothesNo FROM postcount INTERSECT SELECT clothesNo FROM post))"+" "+
                  "OR (post.coatNo IN (SELECT coatNo FROM postcount INTERSECT SELECT coatNo FROM post))"+" "+
                  "AND (post.pantsNo IN (SELECT pantsNo FROM postcount INTERSECT SELECT pantsNo FROM post))"+" "+
                  "OR (post.shoesNo IN (SELECT shoesNo FROM postcount INTERSECT SELECT shoesNo FROM post))"+" "+
                  "OR (post.accessoriesNo IN (SELECT accessoriesNo FROM postcount INTERSECT SELECT accessoriesNo FROM post))")

orACCOSHPASearchSQLCmd = ("SELECT * FROM post"+" "+
                  "WHERE (post.styleNo IN (SELECT styleNo FROM postcount INTERSECT SELECT styleNo FROM post))"+" "+
                  "AND (post.clothesNo IN (SELECT clothesNo FROM postcount INTERSECT SELECT clothesNo FROM post))"+" "+
                  "OR (post.coatNo IN (SELECT coatNo FROM postcount INTERSECT SELECT coatNo FROM post))"+" "+
                  "OR (post.pantsNo IN (SELECT pantsNo FROM postcount INTERSECT SELECT pantsNo FROM post))"+" "+
                  "OR (post.shoesNo IN (SELECT shoesNo FROM postcount INTERSECT SELECT shoesNo FROM post))"+" "+
                  "OR (post.accessoriesNo IN (SELECT accessoriesNo FROM postcount INTERSECT SELECT accessoriesNo FROM post))")

# orIncreasing
# ------------------------------------------------------------------------------------------------------------------------------------------------

# ---分析貼文內容用SQL---

sentenceAnalysisSQLCmd = ("SELECT webSentence.* FROM webSentence, userSentenceCount WHERE webSentence.sentence LIKE '%' + userSentenceCount.userSentence + '%'")
