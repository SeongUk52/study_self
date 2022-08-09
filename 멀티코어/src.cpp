#include <iostream>
#include <vector>
#include <algorithm>

constexpr size_t DIM = 3;
#define SAFE_DELETE(p) { if(p){ delete(p); p=nullptr; }}
class KdTree
{
private:
	struct NODE {
		float pos[DIM];
		NODE* left, * right;
		NODE(const float pos[DIM])
			: left{ nullptr }, right{ nullptr }{
			memcpy(this->pos, pos, sizeof(float) * 3);
		}
		~NODE() {
			SAFE_DELETE(left);
			SAFE_DELETE(right);
		}
	};
	NODE* root;
public:
	KdTree() :root(nullptr) {}
	virtual ~KdTree() { SAFE_DELETE(root); }
public:
	void insert(const float pos[DIM]) {
		this->insert(pos, root, 0);
	}
	void insert(std::initializer_list<float> pos) {
		float v[DIM]{ };
		auto iter{ pos.begin() };
		for (size_t i{ 0 }; i < DIM; ++iter, ++i) v[i] = *iter;
		this->insert(v);
	}
	const NODE* getNN(const float pos[DIM]) {
		return this->getNN(pos, this->root, 0);
	}
private:
	void insert(const float pos[DIM],
		NODE*& parent, int level) {
		if (!parent) parent = new NODE(pos);
		else if (pos[level] < parent->pos[level])
			insert(pos, parent->left, (level + 1) % DIM);
		else	insert(pos, parent->right, (level + 1) % DIM);
	}
	const float distance(const float a[DIM], const float b[DIM]) {
		float ret{ 0.0f };
		for (size_t i{ 0 }; i < DIM; ++i)
			ret += std::pow((a[i] - b[i]), 2);
		return std::sqrt(ret);
	}
	const NODE* closest(const float pos[DIM], const NODE* a, const NODE* b) {
		if (!a) return b;
		if (!b) return a;
		double d1 = distance(pos, a->pos);
		double d2 = distance(pos, b->pos);
		if (d1 < d2)	return a;
		else			return b;
	}
	const NODE* getNN(const float pos[DIM], const NODE* cur, int depth) {
		if (!cur) return nullptr;
		bool flag = pos[depth % DIM] < cur->pos[depth % DIM];
		NODE* next{ flag ? cur->left : cur->right };
		NODE* other{ flag ? cur->right : cur->left };

		const NODE* temp = getNN(pos, next, depth + 1);
		const NODE* best{ closest(pos, temp, cur) };
		float r = this->distance(pos, best->pos);
		float dr = pos[depth % DIM] - cur->pos[depth % DIM];
		if (r >= dr * dr) {
			temp = getNN(pos, other, depth + 1);
			best = closest(pos, temp, best);
		}

		return best;
	}
};

class KdTree_Array
{
	struct FLAG_POS {
		bool flag{ false };
		float pos[DIM];
		void set(const float pos[DIM]) {
			flag = true;
			for (size_t i{ 0 }; i < DIM; ++i)
				this->pos[i] = pos[i];
		}
	};
	std::vector<FLAG_POS> nodes;
public:
	KdTree_Array() = default;
	KdTree_Array(std::vector<std::vector<int>>& items) {
		/*
		KdTree_Array(items.size());

		std::sort(items.begin(), items.end(), [](const std::vector<int>& a, const std::vector<int>& b) { return a[0] < b[0]; });
		auto sortedX = items;
		std::sort(items.begin(), items.end(), [](const std::vector<int>& a, const std::vector<int>& b) { return a[1] < b[1]; });
		auto sortedY = items;
		std::sort(items.begin(), items.end(), [](const std::vector<int>& a, const std::vector<int>& b) { return a[2] < b[2]; });
		auto sortedZ = items;
		*/
	}
	KdTree_Array(int capacity) { nodes.resize(capacity); }
public:
	void insert(std::initializer_list<float> pos) {
		float v[DIM]{ };
		auto iter{ pos.begin() };
		for (size_t i{ 0 }; i < DIM; ++iter, ++i) v[i] = *iter;
		this->insert(v);
	}
	void insert(const float pos[DIM]) { this->insert(pos, 0, 0); }
	void printNodes(const size_t idx = 0) {
		if (idx >= nodes.size() || !nodes[idx].flag) return;
		std::cout << '\n' << idx << ": ";
		for (int i = 0; i < DIM; ++i)
			std::cout << nodes[idx].pos[i] << ' ';
		printNodes(left(idx));
		printNodes(right(idx));
	}
	const int getNN(const float pos[DIM]) {
		return this->getNN(pos, 0, 0);
	}
private:
	size_t left(const size_t parent_idx) { return parent_idx * 2 + 1; }
	size_t right(const size_t parent_idx) { return parent_idx * 2 + 2; }

	void insert(const float pos[DIM], size_t parent, unsigned int level) {
		if (parent >= nodes.size()) return;
		if (!nodes[parent].flag) nodes[parent].set(pos);
		else if (pos[level] <= nodes[parent].pos[level])
			insert(pos, left(parent), (level + 1) % DIM);
		else insert(pos, right(parent), (level + 1) % DIM);
	}

	const float distance(const float a[DIM], const float b[DIM]) {
		float ret{ 0.0f };
		for (size_t i{ 0 }; i < DIM; ++i)
			ret += std::pow((a[i] - b[i]), 2);
		return std::sqrt(ret);
	}
	const size_t closest(const float pos[DIM], const size_t a, const size_t b) {
		if (a >= nodes.size() || !nodes[a].flag) return b;
		if (b >= nodes.size() || !nodes[b].flag) return a;
		double d1 = distance(pos, nodes[a].pos);
		double d2 = distance(pos, nodes[b].pos);
		if (d1 < d2)	return a;
		else			return b;
	}
	const int getNN(const float pos[DIM], const size_t cur, int depth) {
		if (!nodes[cur].flag) return -1;
		bool flag = pos[depth % DIM] < nodes[cur].pos[depth % DIM];
		size_t next{ flag ? left(cur) : right(cur) };
		size_t other{ flag ? right(cur) : left(cur) };

		int temp = getNN(pos, next, depth + 1);
		size_t best{ closest(pos, temp, cur) };
		float r = this->distance(pos, nodes[best].pos);
		float dr = pos[depth % DIM] - nodes[cur].pos[depth % DIM];
		if (r >= dr * dr) {
			temp = getNN(pos, other, depth + 1);
			best = closest(pos, temp, best);
		}

		return best;
	}
};

int main(void)
{
	KdTree_Array kt(1000);
	kt.insert({ 6, 5, 2 });
	kt.insert({ 1, 8, 9 });
	kt.insert({ 7, 1, 1 });
	kt.insert({ 7, 8, 7 });
	kt.insert({ 7, 3, 6 });
	kt.insert({ 2, 1, 4 });
	kt.insert({ 1, 4, 1 });
	kt.insert({ 8, 7, 3 });
	kt.insert({ 6, 2, 8 });
	kt.insert({ 2, 8, 6 });
	kt.insert({ 9, 1, 4 });
	kt.insert({ 2, 8, 3 });
	kt.insert({ 8, 1, 4 });
	kt.insert({ 9, 4, 1 });
	kt.insert({ 7, 2, 9 });
	kt.printNodes();


	float target[DIM] = { 2, 8, 2 };
	std::cout << '\n' << kt.getNN(target) << std::endl;

	/*
	std::vector<std::vector<int>> items = {
		{3, 2, 0}, {5, 8, 0}, {6, 1, 0}, {9, 0, 0},
		{4, 4, 0}, {1, 1, 0}, {2, 2, 0}, {8, 7, 0}
	};
	sort(items);
	*/
}