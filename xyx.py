def count_characters(text):
  output = ""
  current_char = None
  current_count = 0
  for char in text:
    if char == current_char:
      current_count += 1
    else:
      if current_char is not None:
        output += str(current_count) + current_char
      current_char = char
      current_count = 1
  output += str(current_count) + current_char  # Append the last character and count
  return output

# Example usage
text = "aabbcde"

counted_string = count_characters(text)
print(counted_string)

a=counted_string
b = "3sj5iy9k280"

merged_string = ""
for i in range(len(a)):
    merged_string += a[i] + b[i]


if len(b) > len(a):
    merged_string += b[len(a):]

print(merged_string)


def merge_char_count_with_multiple_hyphens(text1, count_text):

  output = ""
  if len(text1) != len(count_text):
      raise ValueError("Strings must have the same length")  # Handle unequal lengths

  for i in range(len(text1)):
      output += "-" * (int(count_text[i]) + 1) + "-" + text1[i]  # Add hyphens based on count

  return output


# Example usage
text1 = counted_string
count_text = "2a2b1c1d1e"

merged_string = merge_char_count_with_multiple_hyphens(text1, count_text)
print(merged_string)