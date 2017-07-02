%%%%%

a_length = 10;
A = round(rand([1,a_length])*a_length/3 + 1)

%A = [2,3,1,1,4]
%A = [2,3,1,1,4,2,4,3,4]

% Forward
Jumps = zeros(length(A),length(A));
for i1 = 1:size(Jumps,2)
    jumps_temp = zeros(1,size(Jumps,2));
    for i2 = 1:A(i1)
        if i1 + i2 <= length(jumps_temp)
            jumps_temp(i1 + i2) = i1
        end
    end
    Jumps(i1,:) = jumps_temp;
end

Jumps

%%%% Tree
c_indx = 1
Tree_m = [c_indx, zeros(1, size(A,2) - 1)]
branch_check = 0

for i0 = 1:1000
    if branch_check(i0) == 0
        tree_m_temp = Tree_m(i0,:);
        jumps_temp = Jumps(max(tree_m_temp),:);
        find(jumps_temp == max(tree_m_temp))
        n_indx_p = find(jumps_temp == max(tree_m_temp));
        for i2 = 1:size(n_indx_p,2)
            tree_m_temp2 = tree_m_temp;
            tree_m_temp2(min(find(tree_m_temp == 0))) = n_indx_p(i2)
            Tree_m = [Tree_m; tree_m_temp2];
        end
        branch_check(i0) = 1;
        branch_check = [branch_check; zeros(size(n_indx_p,2),1)];
    end
    Tree_m;
    
    if    i0 + 1 > size(Tree_m,1)
        break
    end
end
Tree_m


%%% Brutal force /Stochastic way
c_indx = 1
sh_m = [c_indx, zeros(1, size(A,2) - 1)]
step = 1
gl_m = []
for i0 = 1:1000
    jumps_temp = Jumps(c_indx,:);
    step = step + 1;
    n_indx_p = find(jumps_temp == c_indx);
    n_indx = n_indx_p(round(rand(1) * (length(n_indx_p)-1)) + 1);
    sh_m(step) = n_indx;
    if n_indx == size(A,2)
        gl_m_eval = 1;
        for i1 = 1:size(gl_m,1)
            gl_m_temp = gl_m(i1,:);
            gl_m_eval = gl_m_eval*(gl_m_temp - sh_m)*(gl_m_temp - sh_m)';
        end
        if gl_m_eval ~= 0
            gl_m = [gl_m; sh_m];
            sh_m = sh_m;
        end
        %%%% From the begining
        c_indx = 1;
        sh_m = [c_indx, zeros(1, size(A,2) - 1)];
        step = 1;
    else
        p_indx = c_indx;
        c_indx = n_indx;
    end

end
gl_m
