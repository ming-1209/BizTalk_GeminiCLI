const API_BASE = window.location.origin;

document.addEventListener('DOMContentLoaded', () => {
    const targetBtns = document.querySelectorAll('.target-btn');
    const convertBtn = document.getElementById('convertBtn');
    const copyBtn = document.getElementById('copyBtn');
    const inputText = document.getElementById('inputText');
    const outputText = document.getElementById('outputText');
    const outputSection = document.getElementById('outputSection');
    const loading = document.getElementById('loading');

    // 수신 대상 선택 이벤트
    targetBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            targetBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });

    // 변환하기 버튼 클릭 이벤트
    convertBtn.addEventListener('click', async () => {
        const text = inputText.value.trim();
        const activeBtn = document.querySelector('.target-btn.active');
        const target = activeBtn ? activeBtn.dataset.target : null;

        if (!text) {
            alert('전달하고 싶은 내용을 입력해주세요.');
            return;
        }

        if (!target) {
            alert('수신 대상을 선택해주세요.');
            return;
        }

        // 로딩 표시 시작
        loading.style.display = 'flex';
        outputSection.style.display = 'none';

        try {
            const response = await fetch(`${API_BASE}/api/convert`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text: text,
                    target_audience: target
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || '변환 중 오류가 발생했습니다.');
            }

            const data = await response.json();
            outputText.value = data.converted_text;
            outputSection.style.display = 'block';
            
            // 결과창으로 스크롤
            outputSection.scrollIntoView({ behavior: 'smooth' });

        } catch (error) {
            console.error('Error:', error);
            alert(`오류: ${error.message}`);
        } finally {
            // 로딩 표시 종료
            loading.style.display = 'none';
        }
    });

    // 복사하기 버튼 클릭 이벤트
    copyBtn.addEventListener('click', () => {
        outputText.select();
        document.execCommand('copy');
        
        const originalText = copyBtn.innerText;
        copyBtn.innerText = '복사 완료! ✅';
        copyBtn.style.color = '#059669';
        
        setTimeout(() => {
            copyBtn.innerText = originalText;
            copyBtn.style.color = '';
        }, 2000);
    });
});
