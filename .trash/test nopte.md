```yaml enhanced-tables

# date-format: DD-MM-YYYY
yes-format: "yes"
no-format: "no"

columns:
  Number column:
    alias: numberColumn
    type: number
    number-format: "style: 'currency', currency: 'EUR'"
  Date:
    type: date
    date-format: YYYY/MM/DD
  Formatted:
    formatter: "`#${$row.Id}) ${$cell}`"
    nowrap: true
  Hidden:
    hidden: true
  Rating:
    type: enum
    enum:
      '1': '⭐️'
      '2': '⭐️⭐️'
      '3': '⭐️⭐️⭐️'
      '4': '⭐️⭐️⭐️⭐️'
      '5': '⭐️⭐️⭐️⭐️⭐️'
  Boolean:
    type: bool
    yes-format: '👍'
    no-format: '👎'
filter: $row.numberColumn > 1200
filters:
 Small numbers: $row.numberColumn < 1200
 High rating: Number($row.Rating) > 3
& $row.numberColumn == 1500
sort: Rating
# sort: -Rating
pagination:
  page-size: 5
  page-sizes:
   - 5
   - 10
style: |
   th {
     background-color: var(--color-base-50) !important;
     color: var(--color-base-70) !important;
   }
# hide-controls: true
hide-configuration: false
```
|     | Id  | Number column | Date       | Rating | Formatted  | Hidden             | Boolean  |
| --- | --- | ------------- | ---------- | ------ | ---------- | ------------------ | -------- |
|     | 1   | 500           | 01-01-2024 | 2      | _**bold**_ | Text you won't see |          |
|     | 2   | 1000          | 07-02-2024 | 5      |            |                    | no       |
|     | 3   | 1500          | 11-06-2024 | 1      | green      |                    | yes      |
|     |     |               |            |        |            |                    |          |
|     | 4   | 10000         | 05-01-2024 | 4      | ~~strike~~ |                    | whatever |