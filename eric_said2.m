function eric_said2

%keyboard; 
% It is challenging to avoide O(N^2)...
% My first try. 


%%% Initial Matrix
m = 4
n = 6

A = round(rand(m,n));


m_max = max(sum(A,1))
n_max = max(sum(A,2))
p_rec_max = sum(sum(A))

a_vec = A(:);

mask_stack_unique = [];
mask_stack = [];
for i1 = 1:m_max
    for i2 = 1:n_max
        Mask = zeros(m,n);
        Mask([1:i1],[1:i2]) = 1;

        if sum(sum(Mask)) > p_rec_max || sum(sum(Mask)) > m_max * n_max
            break
        else

            mask = Mask(:);
            mask_stack_unique = [mask_stack_unique, mask];
            mask_stack = [mask_stack, mask];
            mask_shift = mask;
            wrap_line = i1;
            for i3 = 1:n*m
                mask_shift([2:end]) = mask_shift([1:end-1]);
                mask_shift(1) = 0;
                
                if rem(i3,m) + i1 <= m %&& %rem(i3,m) ~= 0
                    mask_stack = [mask_stack, mask_shift];
                end
                if mask_shift(end) == 1
                    break
                end
             
            end
        end
    end
end

figure(1)
imagesc(mask_stack)

rect_eval1 = a_vec' * mask_stack;
loc1 = find(rect_eval1 == sum(mask_stack,1));
rect_eval2 = rect_eval1(find(rect_eval1 == sum(mask_stack,1)));
max(rect_eval2)
loc2 = loc1(find(rect_eval2 == max(rect_eval2)))

Mask_2 = zeros(size(A));
for i1 = 1:length(loc2)
    mask_2 = mask_stack(:,loc2(i1));
    Mask_2_temp = reshape(mask_2,[m,n]);
    %if max(sum(Mask_2_temp,2)) * max(sum(Mask_2_temp,1)) == max(rect_eval2)
    wrap_eval_h = sum(Mask_2_temp,1);
    wrap_eval_v = sum(Mask_2_temp,2);
    wrap_eval_h = wrap_eval_h(find(wrap_eval_h ~= 0 ));
    wrap_eval_v = wrap_eval_v(find(wrap_eval_v ~= 0 ));
    if std(wrap_eval_h) == 0 &&  std(wrap_eval_v) == 0
        Mask_2 = Mask_2 + reshape(mask_2,[m,n]);
    end
end

figure(2);
subplot(131); imagesc(A); axis square;
subplot(132); imagesc(Mask_2); axis square;
subplot(133); imagesc(A + Mask_2); axis square;


