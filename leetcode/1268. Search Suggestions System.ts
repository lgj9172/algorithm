function suggestedProducts(products: string[], searchWord: string): string[][] {
  products.sort();
  const answer = [];
  let typedWord = "";
  for (const searchCharacter of searchWord) {
    typedWord += searchCharacter;
    answer.push(
      products.filter((product) => product.indexOf(typedWord) === 0).slice(0, 3)
    );
  }
  return answer;
}
