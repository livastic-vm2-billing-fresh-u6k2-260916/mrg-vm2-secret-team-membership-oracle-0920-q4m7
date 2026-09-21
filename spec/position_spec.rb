RSpec.describe 'position group' do
  it 'different new regression' do
    puts "VM2_ID=#{RSpec.current_example.id}"
    raise 'VM2 contributor regression'
  end

  it 'intended quarantined test' do
    puts "VM2_ID=#{RSpec.current_example.id}"
  end
end
