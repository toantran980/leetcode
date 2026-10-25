# Given a tensor of logits representing next-token scores from a language model, implement Top-k sampling without torch.topk: manually identify the k highest-logit tokens, normalize probabilities over only that subset, and sample one token according to the resulting distribution. Handle invalid temperature safely by requiring temperature > 0.

# Constraints
# Input: logits (1D torch.Tensor), k (int, k > 0), optional temperature (float, temperature > 0)
# Output: sampled token index (int)
# Do not use torch.topk directly for sampling; implement selection manually, e.g. via torch.sort.
# Examples
# Input: logits = torch.tensor([2.0, 1.0, 0.1, 0.5]), k = 2, temperature = 1.0

# Output: Sampled index is either 0 or 1, with probabilities proportional to softmax([2.0, 1.0])

# Explanation: Sort logits descending, keep the largest 2 values manually (without torch.topk), normalize only that subset, then map the sampled local position back to the original index.

 

# Input: logits = torch.tensor([2.0, 1.0, 0.1]), k = 5, temperature = 1.0

# Output: Equivalent to sampling from all 3 tokens

# Explanation: Clamp k to vocab size before sorting/selecting.

 

# Input: logits = torch.tensor([2.0, 1.0, 0.1]), k = 2, temperature = 0

# Output: Raise ValueError

# Explanation: Temperature must be strictly positive to avoid invalid scaling.

import torch
import torch.nn.functional as F

class Solution:
    def top_k_sample(self, logits: torch.Tensor, k: int, temperature: float = 1.0) -> int:
        # logits: 1D tensor of shape (vocab_size,)
        if logits.dim() != 1 or logits.numel() == 0:
            raise ValueError("logits must be a non-empty 1D tensor")
        if k <= 0:
            raise ValueError("k must be positive")
        if temperature <= 0:
            raise ValueError("temperature must be > 0")

        k = min(k, logits.size(0))

        # Manually get top-k via sort (do not use torch.topk)
        sorted_vals, sorted_idx = torch.sort(logits, descending=True)
        topk_vals = sorted_vals[:k] / temperature
        topk_idx = sorted_idx[:k]

        # Softmax over the top-k subset only
        probs = F.softmax(topk_vals, dim=-1)

        # Sample a local position, then map back to the original token index
        sampled_local = torch.multinomial(probs, num_samples=1).item()
        sampled_token = topk_idx[sampled_local].item()
        return sampled_token

def main():
    sol = Solution()

    # Test 1: only indices 0 and 1 appear, with ~73% / 27% frequencies
    logits = torch.tensor([2.0, 1.0, 0.1, 0.5])
    counts = {}
    n = 10000
    for _ in range(n):
        t = sol.top_k_sample(logits, k=2, temperature=1.0)
        counts[t] = counts.get(t, 0) + 1
    print("counts:", counts)
    print("freq of 0:", counts.get(0, 0) / n, "(expected ~0.731)")
    assert set(counts) <= {0, 1}, "sampled a token outside the top-k"

    # Test 2: k larger than vocab is clamped to vocab size
    small = torch.tensor([2.0, 1.0, 0.1])
    out = sol.top_k_sample(small, k=5, temperature=1.0)
    assert out in {0, 1, 2}
    print("k clamp ok:", out)

    # Test 3: k = 1 is greedy, always returns the argmax
    for _ in range(100):
        assert sol.top_k_sample(logits, k=1) == 0
    print("k=1 greedy ok")

    # Test 4: invalid temperature raises ValueError
    for bad_temp in (0, -1.0):
        try:
            sol.top_k_sample(small, k=2, temperature=bad_temp)
            raise AssertionError("expected ValueError")
        except ValueError as e:
            print(f"temperature={bad_temp} -> ValueError:", e)

    # Test 5: invalid k raises ValueError
    try:
        sol.top_k_sample(small, k=0)
        raise AssertionError("expected ValueError")
    except ValueError as e:
        print("k=0 -> ValueError:", e)

    print("all tests passed")


if __name__ == "__main__":
    main()