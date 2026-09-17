public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        // To sort a string you need to convert it to a char array

        List<List<string>> final = new List<List<string>>();
        Dictionary<string, List<string>> dict = new Dictionary<string, List<string>>();

        for (int i = 0; i < strs.Length; i++){
            //Console.WriteLine(strs[i]);
            char[] charArray = strs[i].ToCharArray();
            string unsorted = new String(charArray);
            Array.Sort(charArray);
            string sorted = new string(charArray);
            //Console.WriteLine(sorted);

            if (dict.ContainsKey(sorted)){
                dict[sorted].Add(unsorted);
            }
            else {
                dict[sorted] = new List<string> { unsorted };
            }            
        }

        return new List<List<string>>(dict.Values);
    }
}
