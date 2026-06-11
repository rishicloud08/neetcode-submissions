public class Solution {
    public List<int> FindDisappearedNumbers(int[] nums) {
        int endValue = nums.Length;
        List<int> testList = new List<int>();
        List<int> result = new List<int>();
        for(int i = 1; i <= endValue; i++)
            testList.Add(i);
        foreach(int number in testList)
            if(!(nums.Contains(number)))
                result.Add(number);
        return result;
    }
}