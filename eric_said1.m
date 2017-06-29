function eric_said1

keyboard; 

r = randi([0 50],1,100) % 

key_num = 24

key_vec = key_num .* ones(size(r));

r_corr = key_vec - r; 

paird_r = ismember(r,r_corr)

rslt1 = [find(paird_r)',r(find(paird_r))',r_corr(find(paird_r))']

%%%
rslt2 = sortrows(rslt1,2)