
    static class DNode {
        DNode parent;
        int data;
        int height = 1;
        DNode(int data) {
            this.data = data;
        }
    }

    DNode find(DNode x) {
        if(x.parent == null) {
            return x;
        }
        DNode root = find(x.parent);
        x.parent = root;
        return root;
    }

    DNode union(DNode x, DNode y) {
        DNode xRoot = find(x), yRoot = find(y);
        if(xRoot != yRoot) {
            if(xRoot.height >= yRoot.height) {
                xRoot.parent = yRoot;
                yRoot.height = Math.max(yRoot.height, xRoot.height + 1);
                return yRoot;
            } else {
                yRoot.parent = xRoot;
                xRoot.height = Math.max(xRoot.height, yRoot.height + 1);
                return xRoot;
            }
        }
        return xRoot;
    }

    DNode make(int data) {
        return new DNode(data);
    }
